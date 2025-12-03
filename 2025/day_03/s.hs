import Data.Char (digitToInt)
import Data.List (minimumBy)

maxAndIndex :: [Int] -> (Int, Int)
maxAndIndex l = minimumBy (\x y -> compare (-snd x) (-snd y)) (zip [0 ..] l)

pickBest :: [Int] -> Int -> [Int]
pickBest s 0 = []
pickBest s tot = best : pickBest rem (tot - 1)
  where
    budget = length s - tot + 1
    toPickFrom = take budget s
    (bestIndex, best) = maxAndIndex toPickFrom
    rem = drop (bestIndex + 1) s

listToInt :: [Int] -> Int
listToInt = foldl (\acc x -> acc * 10 + x) 0

joltage :: [Int] -> Int -> Int
joltage battery n = listToInt $ pickBest battery n

main :: IO ()
main = do
  input <- lines <$> readFile "input.txt"
  let batteries = map (map digitToInt) input

  let part1 = sum $ map (`joltage` 2) batteries
  print part1

  let part2 = sum $ map (`joltage` 12) batteries
  print part2
