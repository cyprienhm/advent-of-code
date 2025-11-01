moveSubmarine :: (Int, Int) -> (String, Int) -> (Int, Int)
moveSubmarine (depth, distance) ("forward", amount) = (depth, distance + amount)
moveSubmarine (depth, distance) ("up", amount) = (depth - amount, distance)
moveSubmarine (depth, distance) ("down", amount) = (depth + amount, distance)

main :: IO ()
main = do
  contents <- readFile "input.txt"
  let contentsLines = (takeWhile (/= "") . lines) contents
  let splitWords = map words contentsLines
  let tuples = map (\[x, y] -> (x, read y :: Int)) splitWords
  let (depth, distance) = foldl moveSubmarine (0, 0) tuples
  print depth
  print distance
  print (depth * distance)

  return ()
