import Data.Char

batch :: Int -> [String] -> [[String]]
batch n [] = []
batch n s = take n s : (batch n . drop n) s

inOthers :: Char -> [String] -> Bool
inOthers c = all (\x -> c `elem` x)

common :: [String] -> Char
common bags = (head . filter (\x -> (inOthers x . tail) bags) . head) bags

score :: Char -> Int
score c
  | isUpper c = ord c - ord 'A' + 27
  | isLower c = ord c - ord 'a' + 1

main :: IO ()
main = do
  bags <- takeWhile (/= "") . lines <$> readFile "./input.txt"

  let groups3 = batch 3 bags
  let badges = map common groups3

  let res = (sum . map score) badges
  print res
