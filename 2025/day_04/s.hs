import Data.Set (Set)
import qualified Data.Set as Set

aroundDirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

accessible :: (Int, Int) -> Set (Int, Int) -> Bool
accessible (row, col) grid = length around < 4
  where
    around = filter id [(row + up, col + right) `Set.member` grid | (up, right) <- aroundDirs]

removeRolls :: Set (Int, Int) -> (Int, Set (Int, Int))
removeRolls grid
  | null toRemove = (0, grid)
  | otherwise = (length toRemove, Set.filter (`Set.notMember` toRemove) grid)
  where
    toRemove = Set.filter (`accessible` grid) grid

removeMaxRolls :: Set (Int, Int) -> Int
removeMaxRolls grid
  | removed == 0 = 0
  | otherwise = removed + removeMaxRolls newGrid
  where
    (removed, newGrid) = removeRolls grid

main :: IO ()
main = do
  grid <- lines <$> readFile "input.txt"

  let positions = [(row, col) | row <- [0 .. length grid - 1], col <- [0 .. length (head grid) - 1]]
  let rolls = Set.fromList (filter (\(row, col) -> (grid !! row !! col) == '@') positions)
  let accessibleRolls = Set.filter (`accessible` rolls) rolls

  print $ length accessibleRolls
  print $ removeMaxRolls rolls
