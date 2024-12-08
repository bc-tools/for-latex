io.write("Qui êtes-vous ? ")
local name = io.read()

if name == "" then
    print("Ah, pas très bavard aujourd'hui !")

else
    print("Bonjour " .. name .. ".")
    print("Épatant ! En fait, pas du tout...")
end
