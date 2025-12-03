splitOn :: Char -> String -> [String]
splitOn sep "" = []
splitOn sep s = takeWhile (/= sep) s : splitOn sep stuff
  where
    rest = dropWhile (/= sep) s
    stuff
      | null rest = ""
      | length rest == 1 = rest
      | otherwise = tail rest

invalidp1 :: Int -> Bool
invalidp1 n =
  let ns = show n; halfLen = length ns `div` 2
   in take halfLen ns == drop halfLen ns

rangeToInvalids :: (Int -> Bool) -> [Int] -> [Int]
rangeToInvalids invFun [low, hi] = filter invFun [low .. hi]

part1 :: [[Int]] -> Int
part1 ranges = let invalids = map (sum . rangeToInvalids invalidp1) ranges in sum invalids

patternInNum :: String -> String -> Bool
patternInNum subset ns
  | subLength > length ns = False
  | subset == ns = True
  | otherwise = (subset == take subLength ns) && patternInNum subset (drop subLength ns)
  where
    subLength = length subset

invalidp2 :: Int -> Bool
invalidp2 n =
  let ns = show n; lengthes = [1 .. length ns `div` 2]
   in or [patternInNum (take l ns) ns | l <- lengthes]

part2 :: [[Int]] -> Int
part2 ranges = let invalids = map (sum . rangeToInvalids invalidp2) ranges in sum invalids

main :: IO ()
main = do
  input <- head . lines <$> readFile "example.txt"
  let rangesStr = splitOn ',' input
  let ranges = map (map (\x -> read x :: Int) . splitOn '-') rangesStr

  print (part1 ranges)
  print (part2 ranges)
