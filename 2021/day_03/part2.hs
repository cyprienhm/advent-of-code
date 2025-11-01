import Data.Char (digitToInt)

sumFirstElement :: [[Int]] -> Int
sumFirstElement l = sum (map (\(x : _) -> x) l)

getMajority :: Int -> Int -> (Int -> Int -> Bool) -> Int
getMajority count len condition | condition count len = 1 | otherwise = 0

maxMajority :: Int -> Int -> Bool
maxMajority count len = 2 * count >= len

minMajority :: Int -> Int -> Bool
minMajority count len = 2 * count < len

belongsMajority :: [Int] -> Int -> Bool
belongsMajority (1 : _) 1 = True
belongsMajority (0 : _) 1 = False
belongsMajority (1 : _) 0 = False
belongsMajority (0 : _) 0 = True

getRating :: [[Int]] -> (Int -> Int -> Bool) -> [Int]
getRating [l] majorityCondition = l
getRating l majorityCondition =
  let majorityBit = getMajority (sumFirstElement l) (length l) majorityCondition
   in let filterMajority l = belongsMajority l majorityBit
       in let filteredList = filter filterMajority l
           in majorityBit : getRating (map tail filteredList) majorityCondition

binary2int :: [Int] -> Int
binary2int [] = 0
binary2int (x : xs) = x + 2 * binary2int xs

main :: IO ()
main = do
  digits <- map (map digitToInt) . lines <$> readFile "./input.txt"
  let len = length digits

  let oxygenRating = getRating digits maxMajority
  let co2Rating = getRating digits minMajority

  let oxygenRatingDecimal = binary2int (reverse oxygenRating)
  let co2RatingDecimal = binary2int (reverse co2Rating)

  print (oxygenRatingDecimal * co2RatingDecimal)
