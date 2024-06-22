import pandas as pd


data_completa = {
    "Comando": [
        "<html>", "<head>", "<title>", "<body>", "<h1> a <h6>", "<p>", "<a>", "<div>", "<span>", "<table>", "<tr>", "<td>", "<th>", "<thead>", "<tbody>", "<tfoot>", 
        "<caption>", "<col>", "<colgroup>", "<ul>", "<ol>", "<li>", "<dl>", "<dt>", "<dd>", "<form>", "<input>", "<textarea>", "<button>", "<select>", "<option>", 
        "<label>", "<fieldset>", "<legend>", "<datalist>", "<output>", "<iframe>", "<img>", "<figure>", "<figcaption>", "<audio>", "<video>", "<source>", "<track>", 
        "<canvas>", "<svg>", "<math>", "<embed>", "<object>", "<param>", "<blockquote>", "<q>", "<cite>", "<code>", "<pre>", "<samp>", "<kbd>", "<var>", "<mark>", 
        "<time>", "<progress>", "<meter>", "<b>", "<i>", "<u>", "<strong>", "<em>", "<small>", "<del>", "<ins>", "<sub>", "<sup>", "<abbr>", "<address>", "<bdo>", 
        "<ruby>", "<rt>", "<rp>", "<br>", "<wbr>", "<hr>", "<link>", "<meta>", "<style>", "<script>", 
        "<img />", "<br />", "<hr />", "<input />", "<meta />", "<link />", "<source />", "<track />", "<area />", "<base />", "<col />"
    ],
    "Descrição": [
        "Define o documento HTML.", "Contém metadados sobre o documento.", "Define o título do documento.", "Define o corpo do documento.", "Define cabeçalhos.", 
        "Define um parágrafo.", "Define um hiperlink.", "Define uma divisão ou seção.", "Define uma seção em linha.", "Define uma tabela.", "Define uma linha na tabela.", 
        "Define uma célula na tabela.", "Define uma célula de cabeçalho na tabela.", "Define o cabeçalho de uma tabela.", "Define o corpo de uma tabela.", "Define o rodapé de uma tabela.", 
        "Define a legenda de uma tabela.", "Define propriedades de colunas dentro de um <colgroup>.", "Define um grupo de uma ou mais colunas em uma tabela.", 
        "Define uma lista não ordenada.", "Define uma lista ordenada.", "Define um item de lista.", "Define uma lista de descrição.", "Define um termo na lista de descrição.", 
        "Define a descrição de um termo na lista de descrição.", "Define um formulário.", "Define um campo de entrada.", "Define uma área de texto.", "Define um botão.", 
        "Define uma lista suspensa.", "Define uma opção em uma lista suspensa.", "Define um rótulo para um campo de entrada.", "Agrupa elementos relacionados em um formulário.", 
        "Define uma legenda para um <fieldset>.", "Define uma lista de opções predefinidas para um campo <input>.", "Define o resultado de um cálculo.", "Define um iframe.", 
        "Define uma imagem.", "Especifica conteúdo ilustrativo.", "Define uma legenda para um <figure>.", "Define conteúdo de áudio.", "Define conteúdo de vídeo.", 
        "Define múltiplas fontes de mídia para elementos <video> e <audio>.", "Define faixas de texto para elementos <video> e <audio>.", "Usado para desenhar gráficos via script (geralmente JavaScript).", 
        "Define gráficos vetoriais escaláveis.", "Usado para incorporar notações matemáticas.", "Define um contêiner para uma aplicação externa ou conteúdo interativo.", 
        "Define um contêiner para um objeto externo.", "Define parâmetros para um objeto.", "Define uma seção citada de outra fonte.", "Define uma citação curta em linha.", 
        "Define o título de uma obra.", "Define um trecho de código.", "Define texto pré-formatado.", "Define texto de saída de uma amostra de código.", "Define entrada de teclado.", 
        "Define uma variável.", "Define texto marcado.", "Define uma data/hora.", "Representa o progresso de uma tarefa.", "Define uma medida escalar dentro de um intervalo conhecido.", 
        "Define texto em negrito.", "Define texto em itálico.", "Define texto sublinhado.", "Define texto com ênfase forte.", "Define texto com ênfase.", "Define texto pequeno.", 
        "Define texto excluído.", "Define texto inserido.", "Define texto subscrito.", "Define texto sobrescrito.", "Define uma abreviação.", "Define informações de contato.", 
        "Substitui a direção do texto.", "Define uma anotação ruby (anotação de texto).", "Define a anotação ruby.", "Define parênteses ao redor de uma anotação ruby.", 
        "Insere uma quebra de linha.", "Define uma possível quebra de linha.", "Insere uma linha horizontal.", "Define a relação entre um documento e um recurso externo.", 
        "Define metadados sobre um documento HTML.", "Define estilo para um documento HTML.", "Define um script.", 
        "Define uma imagem.", "Insere uma quebra de linha.", "Insere uma linha horizontal.", "Define um campo de entrada.", "Define metadados sobre um documento HTML.", 
        "Define a relação entre um documento e um recurso externo.", "Define múltiplas fontes de mídia para elementos <video> e <audio>.", "Define faixas de texto para elementos <video> e <audio>.", 
        "Define uma área dentro de um mapa de imagem.", "Especifica a URL base para todas as URLs relativas no documento.", "Define propriedades de colunas dentro de um <colgroup>."
    ],
    "Fechamento Automático": [
        "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", 
        "Não", "Não", "Não", "Não", "Sim", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Sim", "Não", "Não", "Não", "Não", "Sim", "Sim", 
        "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", 
        "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Não", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", 
        "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim"
    ]
}

# Verificando os tamanhos das listas
comando_len = len(data_completa["Comando"])
descricao_len = len(data_completa["Descrição"])
fechamento_automatico_len = len(data_completa["Fechamento Automático"])

print(f"Tamanho da lista 'Comando': {comando_len}")
print(f"Tamanho da lista 'Descrição': {descricao_len}")
print(f"Tamanho da lista 'Fechamento Automático': {fechamento_automatico_len}")

# Se os tamanhos forem iguais, crie o DataFrame
if comando_len == descricao_len == fechamento_automatico_len:
    df = pd.DataFrame(data_completa)
    file_path = "comandos_html.xlsx"
    df.to_excel(file_path, index=False)
    print(file_path)
else:
    print("As listas no dicionário 'data_completa' têm comprimentos diferentes.")
