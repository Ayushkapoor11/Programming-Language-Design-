module HW2
     where
import Data.List
-- 1
{- (a) merge2 5%-}

merge2 :: [a] -> [a] -> [a]
merge2 [] [] = []
merge2 [] (x:xs) = (x:xs) 
merge2 (x:xs) [] = (x:xs)
merge2 (x:xs) li = x : merge2 li xs 
                         
{- (b) merge2Tail 10% -}
merge2Tail :: [a] -> [a] -> [a]
merge2Tail [] [] = []
merge2Tail li [] = li
merge2Tail [] li = li
merge2Tail (x:xs) (y:ys) = merge2tailhelper [] (x:xs) (y:ys)

merge2tailhelper :: [a] -> [a] -> [a] -> [a] 
merge2tailhelper acc [] [] = acc
merge2tailhelper acc (x:xs) [] = merge2tailhelper (acc ++ [x]) xs []
merge2tailhelper acc [] (x:xs) = merge2tailhelper (acc ++ [x]) xs []  
merge2tailhelper acc (x:xs) (y:ys) = merge2tailhelper (acc ++ [x]) (y:ys) xs

{- (c) mergeN 5%-}
mergeN:: [[a]] -> [a]
mergeN = foldl merge2 []

-- 2
{- (a) removDuplicates 10% -}
removDuplicates :: Eq a => [a] -> [a]
removDuplicates = foldl (\acc x -> if x `elem` acc then acc else acc ++ [x]) []

{- (b) count 5% -}
count :: Eq a => a -> [a] -> Int
count val = foldr (\x -> if (val == x) then (+1) else (\x -> x)) 0

{- (c) histogram 10% -}
histogram :: Eq a => [a] -> [(a, Int)]
histogram [] = []
histogram [x] = [(x,1)]
histogram (x:xs) = map (count x xs) (,) xs : histogram xs
-- histogram (x:xs) = (x,(count x xs)) : histogram xs
-- 3                
{- (a) concatAll 4% -}
concatAll :: [[String]] -> String
concatAll [[],[]] = ""
concatAll [[x]] = x 
concatAll (x:xs) = foldr (++) "" (helper (x:xs)) 
                                   where helper :: [[String]] -> [String] 
                                         helper (x:xs) = foldl (++) [] (x:xs)

{- (b) concat2Either 9% -}               
data AnEither  = AString String | AnInt Int
                         deriving (Show, Read, Eq)

patternhelper :: AnEither -> AnEither -> AnEither
patternhelper (AString a) (AString b) = AString (a ++ b)
patternhelper (AString a) (AnInt b) = AString (a ++ (show b) )
patternhelper (AnInt a) (AString b) = AString (b ++ (show a))
patternhelper (AnInt a) (AnInt b) = AString ((show (a) ++ show (b)))

concat2Either :: [[AnEither]] -> AnEither
concat2Either [] = AString "" 
concat2Either (x:xs) = singleconcat (map singleconcat (x:xs)) 
                                where singleconcat :: [AnEither] -> AnEither
                                      singleconcat [] = AString ""
                                      singleconcat (x:xs) = (foldl patternhelper x xs)


{- (c) concat2Str 6% -}               
patternhelper2 :: AnEither -> String -> String
patternhelper2 (AString x) y = (x ++ y)
patternhelper2 (AnInt x) y = show x ++ y

concat2Str :: [[AnEither]] -> String
concat2Str [] = "" 
concat2Str (x:xs) = concat (map foldconcat' (x:xs)) 
                    where foldconcat' :: [AnEither] -> String
                          foldconcat' [] = ""
                          foldconcat' (x:xs) = (foldr patternhelper2 "" (x:xs))

-- 4 

data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)

evaluate:: Op -> Int -> Int -> Int
evaluate Add x y =  x+y
evaluate Sub   x y =  x-y
evaluate Mul x y =  x*y
evaluate Pow x y = x^y

data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)

{- (a) evaluateTree - 10% -}
evaluateTree :: ExprTree Int -> Int
evaluateTree (ELEAF x) = x 
evaluateTree (ENODE op t1 t2) = (evaluate op (evaluateTree t1) (evaluateTree t2))

{- (b) printInfix - 10% -}
evaluate':: Op -> Int -> Int -> String
evaluate' Add x y = show (x + y)
evaluate' Sub x y = show (x - y)
evaluate' Mul x y =  show (x * y)
evaluate' Pow x y = show  ( x^y )

printInfix:: Show a => ExprTree a -> String 
printInfix (ELEAF x) = show x
printInfix (ENODE op t1 t2) = "(" ++ printInfix t1 ++ " `" ++ show op ++ "` " ++ printInfix t2 ++ ")" 


{- (c) createRTree 12% -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)

createRTree :: ExprTree Int -> ResultTree Int
createRTree (ELEAF a) = (RLEAF a)
createRTree (ENODE Add t1 t2) = RNODE (evaluateTree t1 + evaluateTree t2)(createRTree t1)(createRTree t2)
createRTree (ENODE Pow t1 t2) = RNODE (evaluateTree t1 ^ evaluateTree t2)(createRTree t1)(createRTree t2)
createRTree (ENODE Mul t1 t2) = RNODE (evaluateTree t1 * evaluateTree t2)(createRTree t1)(createRTree t2)
createRTree (ENODE Sub t1 t2) = RNODE (evaluateTree t1 - evaluateTree t2)(createRTree t1)(createRTree t2)

-- 5
{-Sample trees 4% -}

exprTree3 = (ENODE Mul (ENODE Add (ENODE Add (ELEAF 1)(ELEAF 2)) (ELEAF 6))(ENODE Add (ELEAF 4)(ELEAF 3)))
exprTree4 = (ENODE Add (ENODE Mul (ENODE Add (ELEAF 3)(ELEAF 4)) (ELEAF 6))(ENODE Sub (ELEAF 10)(ELEAF 6)))

--evaluateTree
test1 = evaluateTree exprTree3 --Should return 63
test2 = evaluateTree exprTree4 -- Should return 46
--printInfix
test3 = printInfix exprTree3 --"(((1`Add`2)`Add`6)`Mul`(4`Add`3))"
test4 = printInfix exprTree4 --"(((3`Add`4)`Mul`6)`Add`(10`Sub`6))"
--createRtree
test5 = createRTree exprTree3 --RNODE 63 (RNODE 9 (RNODE 3 (RLEAF 1) (RLEAF 2)) (RLEAF 6)) (RNODE 7 (RLEAF 4) (RLEAF 3))
test6 = createRTree exprTree4 --RNODE 46 (RNODE 42 (RNODE 7 (RLEAF 3) (RLEAF 4)) (RLEAF 6)) (RNODE 4 (RLEAF 10) (RLEAF 6))



