moveSubmarine :: (Int, Int, Int) -> (String, Int) -> (Int, Int, Int)
moveSubmarine (depth, distance, aim) ("forward", amount) = (depth + aim * amount, distance + amount, aim)
moveSubmarine (depth, distance, aim) ("up", amount) = (depth, distance, aim - amount)
moveSubmarine (depth, distance, aim) ("down", amount) = (depth, distance, aim + amount)

main :: IO ()
main = do
  contents <- readFile "input.txt"
  let contentsLines = (takeWhile (/= "") . lines) contents
  let splitWords = map words contentsLines
  let tuples = map (\[x, y] -> (x, read y :: Int)) splitWords
  let (depth, distance, aim) = foldl moveSubmarine (0, 0, 0) tuples
  print depth
  print distance
  print aim
  print (depth * distance)
