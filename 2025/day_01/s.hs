parseInstruction :: String -> Int
parseInstruction s
  | dir == 'L' = -amount
  | dir == 'R' = amount
  where
    dir = head s
    amount = read (tail s) :: Int

countZeros :: (Int, Int) -> Int -> (Int, Int)
countZeros (pos, nZeros) move = (nextPos, nZeros + eqZero)
  where
    nextPos = (pos + move) `mod` 100
    eqZero = if nextPos == 0 then 1 else 0

part1 :: [Int] -> Int
part1 moves = count
  where
    start = 50
    (_finalPos, count) = foldl countZeros (start, 0) moves

countInterZeros :: (Int, Int) -> Int -> (Int, Int)
countInterZeros (pos, nZeros) move = (nextPos, nZeros + interZeros)
  where
    nextPos = (pos + move) `mod` 100
    interZeros = foldl (\tot mov -> tot + case mov of 0 -> 1; _ -> 0) 0 (map (`mod` 100) (tail [pos, pos + (move `div` abs move) .. pos + move]))

part2 :: [Int] -> Int
part2 moves = count
  where
    start = 50
    (_finalPos, count) = foldl countInterZeros (start, 0) moves

main :: IO ()
main = do
  input <- lines <$> readFile "input.txt"
  let moves = map parseInstruction input
  let count1 = part1 moves
  print count1

  let count2 = part2 moves
  print count2
