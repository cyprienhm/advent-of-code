import Data.Char

data Compartments = Compartments
  { comp1 :: String,
    comp2 :: String
  }
  deriving (Show)

compartmentalize :: String -> Compartments
compartmentalize s = Compartments (take half s) (drop half s)
  where
    half = length s `div` 2

common :: Compartments -> Char
common c = head (filter (\x -> x `elem` comp2 c) (comp1 c))

score :: Char -> Int
score c
  | isUpper c = ord c - ord 'A' + 27
  | isLower c = ord c - ord 'a' + 1

main :: IO ()
main = do
  bags <- takeWhile (/= "") . lines <$> readFile "./input.txt"
  let comps = map compartmentalize bags
  let dups = map common comps

  let res = (sum . map score) dups
  print res
