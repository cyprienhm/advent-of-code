import Data.Char (digitToInt)

majority :: (Int -> Int -> Bool) -> Int -> Int -> Int
majority cond len num
  | cond len num = 1
  | otherwise = 0

binary2int :: [Int] -> Int
binary2int [] = 0
binary2int (x : xs) = x + 2 * binary2int xs

main :: IO ()
main = do
  digits <- map (map digitToInt) . lines <$> readFile "./input.txt"
  let len = length digits
  print len
  let counts = foldl (zipWith (+)) (replicate len 0) digits
  print counts
  let gamma = map (majority (\l n -> n * 2 > l) len) counts
  let epsilon = map (majority (\l n -> n * 2 < l) len) counts
  print gamma
  print epsilon
  let gammaInt = (binary2int . reverse) gamma
  let epsilonInt = (binary2int . reverse) epsilon
  print (gammaInt * epsilonInt)
