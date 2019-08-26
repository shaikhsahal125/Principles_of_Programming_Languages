import Data.List.Split


--------------------------------------------------------------------------
-- Hopscotch

skips :: [a] -> [[a]]
skips []   = []
skips [x]  = [[x]]
skips list = [getEveryNth list x | x <- [1..length list]]

-- ****  Helper function for skips to get every Nth element of the list. **

getEveryNth :: [a] -> Int -> [a]
getEveryNth list n = [x |(i, x) <- zip [1..] list, i `mod` n == 0]



-- -----------------------------------------------------------------------
-- 2. Local Maxima

localMaxima :: [Integer] -> [Integer]
localMaxima []               = []
localMaxima [x]              = []
localMaxima [x, y]           = []
localMaxima (x : y : z : zs) = if ((y > x) && (y > z))
                               then y : localMaxima (z : zs)
                               else localMaxima (y : z : zs)



-- ------------------------------------------------------------------------
-- 3. Histogram

histogram :: [Int] -> String
histogram list = reverseOpt (upSideDown list) ++ "==========\n0123456789\n"


-- *********   Helper functions   **********************

reverseOpt :: String -> String
reverseOpt lst =  connect (addN (reverseList (splitList lst)))

upSideDown :: [Int] -> String
upSideDown list = (build (countElem list) (maxFreq (countElem list)))

countElem :: [Int] -> [Int]
countElem lst = [length (count lst x) | x <- [0..9]]

count :: [Int] -> Int -> [Int]
count list n = filter (==n) list

asterisks :: [Int] -> String
asterisks []     = []
asterisks (x:xs) = if x > 0
                   then '*' : asterisks xs
                   else ' ' : asterisks xs

maxFreq :: [Int] -> Int
maxFreq list = maximum list

build :: [Int] -> Int -> String
build [] _ = []
build _ 0 = []
build list n = asterisks list ++ "\n" ++ build (decrementFreq list) (n-1)

decrementFreq :: [Int] -> [Int]
decrementFreq list = map (\x -> x-1) list

splitList :: String -> [String]
splitList st = splitOn "\n" st

reverseList :: [String] -> [String]
reverseList list = reverse list

addN :: [String] -> [String]
addN lst = [x ++ "\n" | x <- lst]

connect :: [String] -> String
connect str = concat str
