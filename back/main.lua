local serjao = require("serjao_berranteiro/serjao_berranteiro")

set_server.use_folder = true
set_server.static_folder = "../front"

---@param rq Request
local function main_server(rq)

  if "/" == rq.route then
    return serjao.send_file("../front/index.html", 200, "text/html")
  end

  return serjao.send_file("../front/error.html", 404, "text/html")
end

serjao.server(3000, main_server)