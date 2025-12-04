aroundDirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

accessible :: (Int, Int) -> [(Int, Int)] -> Bool
accessible (row, col) grid = length around < 4
  where
    around = filter id [(row + up, col + right) `elem` grid | (up, right) <- aroundDirs]

removeRolls :: [(Int, Int)] -> (Int, [(Int, Int)])
removeRolls grid
  | null toRemove = (0, grid)
  | otherwise = (length toRemove, filter (\x -> not $ x `elem` toRemove) grid)
  where
    toRemove = filter (`accessible` grid) grid

removeMaxRolls :: [(Int, Int)] -> Int
removeMaxRolls grid
  | removed == 0 = 0
  | otherwise = removed + removeMaxRolls newGrid
  where
    (removed, newGrid) = removeRolls grid

main :: IO ()
main = do
  input <- lines <$> readFile "input.txt"

  let positions = [(row, col) | row <- [0 .. length input - 1], col <- [0 .. length (head input) - 1]]
  let rolls = filter (\(row, col) -> (input !! row !! col) == '@') positions
  let accessibleRolls = filter (`accessible` rolls) rolls

  print $ length accessibleRolls
  print $ removeMaxRolls rolls
