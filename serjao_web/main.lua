local serjao = require("dependencies/serjao_berranteiro/serjao_berranteiro")
local dtw = require("dependencies/lua/luaDoTheWorld")

set_server.use_folder = true

---@param rq Request
local function main_server(rq)

  if "/" == rq.route then
    return serjao.send_file("pages/index.html", 200, "text/html")
  end

  local rotaSegura = string.gsub(rq.route, "../", "")
  local caminhoRotaFormatada = "pages/" .. rotaSegura .. ".html"

  if dtw.isfile(caminhoRotaFormatada) then
    return serjao.send_file(caminhoRotaFormatada, 200, "text/html")
  end

  return serjao.send_file("pages/404.html", 404, "text.html")

end

serjao.server(3000, main_server)