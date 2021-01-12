-- CptS 355 - Fall 2020  : 09/06/2020
module HW1
     where

import Data.Char

-- 1.a. biggerDate and maxDate
biggerDate::(Ord a1,Ord a2,Ord a3)=>(a3,a2,a1)->(a3,a2,a1)->(a3,a2,a1) 
biggerDate (d1,m1,y1) (d2,m2,y2) | y2 > y1 = (d2,m2,y2)
                                 | y1 > y2 = (d1,m1,y1)
                                 | m2 > m1 = (d2,m2,y2) 
                                 | m1 > m2 = (d1,m1,y1)
                                 | d2 > d1 = (d2,m2,y2)
                                 | d1 > d2 = (d1,m2,y2)
                                 | otherwise = (d1,m1,y1)

-- 1.b. maxDate 
maxDate :: (Ord a1, Ord a2, Ord a3) => [(a3, a2, a1)] -> (a3, a2, a1) 
maxDate [] = error (['4','0','4'])
maxDate [(x)] = x
maxDate (x:xs) = x `biggerDate` maxDate xs

-- 2. ascending
ascending :: Ord t  => [t] -> Bool
ascending [x] = True  -- if list has only one element 
ascending (x:y:xs)  | x <= y = ascending (y:xs)  
                    | otherwise = False 

-- 3.a. insert (-3 4 failed tests of 3a) 
insert :: (Eq a, Num a) => a -> b -> [b] -> [b]
insert 0 item [] = [item]
insert _ item [] = []
insert 1 item [x] = [x] ++ [item]
insert 0 item (x:xs) = item:(x:xs) 
insert n item (x:xs) = x: (insert (n-1) item xs) 

-- 3.b. insertEvery ( -11.4 3b)
insertEvery :: (Eq t, Num t) => t -> a -> [a] -> [a]
insertEvery _ _ [] = []
insertEvery n item (x:xs) = insertEveryhelper n (x:xs)
                                      where insertEveryhelper 0 [] = [item]
                                            insertEveryhelper _ [] = []
                                            insertEveryhelper 0 (x:xs) = item : insertEveryhelper n (x:xs)
                                            insertEveryhelper n (x:xs) = x:insertEveryhelper (n-1) xs

-- 4.a. getHours (-10 )
getSales :: (Num p, Eq t) => t -> [(t, p)] -> p
getSales t [] = 0  
getSales days ((day,sale):xs) | (day == days) = sale + getSales days xs 
                                | otherwise = getSales days xs                    
-- 4.b. sumSales (-10)
sumSales:: (Num p)=> String -> String -> [(String,[(String,p)])] -> p
sumSales store_name days [] = 0
sumSales store_name days ((store,(day,sale):xs):ys) | (store == store_name) && (day == days) = sale + getSales days xs + sumSales store_name days ys 
                                                    | (store == store_name) = getSales days xs + sumSales store_name days ys 
                                                    | otherwise = sumSales store_name days ys
                                                       where getSales :: (Num p, Eq t) => t -> [(t, p)] -> p
                                                             getSales t [] = 0  
                                                             getSales days ((day,sale):rest) | (day == days) = sale + getSales days rest 
                                                                                             | otherwise = getSales days rest 

-- 5.a. split (-6.4 5a)
split :: Eq a => a -> [a] -> [[a]]
split _ [] = [[]]
split c (x:xs) | (x == c) = []:(split c xs) 
               | otherwise = (x:(head (split c xs))):(tail (split c xs))

-- 5.b. nSplit (-15 5b)
nSplit :: (Ord a1, Num a1, Eq a2) => a2 -> a1 -> [a2] -> [[a2]]
nSplit c num [] = [[]]
nSplit c 0 (x:xs) = [(x:xs)]
nSplit c num (x:xs) | (x == c) = []:(nSplit c (num-1) xs) 
                    | otherwise = (x:(head (nSplit c num xs))):(tail (nSplit c num xs))
