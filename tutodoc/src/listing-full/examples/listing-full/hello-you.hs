main :: IO ()

main = do
    putStr "Qui êtes-vous ? "
    name <- getLine

    if name == ""
        then putStrLn "Ah, pas très bavard aujourd'hui !"

        else do
            putStrLn ("Bonjour " ++ name ++ ".")
            putStrLn "Épatant ! En fait, pas du tout..."
