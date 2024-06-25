local serjao = require("serjao_berranteiro/serjao_berranteiro")

--@param request Request
local function main_server(request)
  return "Hello Word", 200
end

serjao.server(3000, main_server)