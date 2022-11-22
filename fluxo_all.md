:::mermaid
sequenceDiagram
Note over AnIA: PRONTUÁRIOS
rect rgba(250, 250, 0, .1)
    AnIA->>Caduceus (Extração): Prontuários
    Note over Caduceus (Extração): Processamento de prontuários
    Caduceus (Extração)->>Caduceus (Consolidação): Medicamentos, Hábitos, Antecedentes, etc
    Note over Caduceus (Consolidação): Detecção de comorbidades e complexidades
    Caduceus (Consolidação)->>HarpIA: Dados consolidados do paciente
    Note over HarpIA: Criação/Atualização de paciente
    HarpIA->>Atlas: Dados consolidados do paciente
    Note over Atlas: Atualização dos dados do paciente
end

Note over AnIA: LAUDOS
rect rgba(0, 250, 250, .1)
    AnIA->>Iris: Laudos
    Note over Iris: Processamento de sentenças e laudos
    Iris->>Caduceus (Consolidação): Alterações detectadas no laudo
    Note over Caduceus (Consolidação): Detecção de comorbidades e complexidades
    Caduceus (Consolidação)->>HarpIA: Dados consolidados do paciente
    Note over HarpIA: Criação/Atualização de paciente
    HarpIA->>Atlas: Dados consolidados do paciente
    Note over Atlas: Atualização dos dados do paciente
end

Note over AnIA: EXAMES LABORATORIAIS
rect rgba(250, 0, 250, .1)
    AnIA->>Caduceus (Consolidação): Exames Laboratoriais
    Note over Caduceus (Consolidação): Detecção de comorbidades e complexidades
    Caduceus (Consolidação)->>HarpIA: Dados consolidados do paciente
    Note over HarpIA: Criação/Atualização de paciente
    HarpIA->>Atlas: Dados consolidados do paciente
    Note over Atlas: Atualização dos dados do paciente
end

Note over AnIA: RECEITAS
rect rgba(0, 127, 128, .1)
    AnIA->>Caduceus (Extração): Receitas
    Note over Caduceus (Extração): Processamento de Receitas
    Caduceus (Extração)->>Caduceus (Consolidação): Medicamentos Extraídos
    Note over Caduceus (Consolidação): Detecção de comorbidades e complexidades
    Caduceus (Consolidação)->>HarpIA: Dados consolidados do paciente
    Note over HarpIA: Criação/Atualização de paciente
    HarpIA->>Atlas: Dados consolidados do paciente
    Note over Atlas: Atualização dos dados do paciente
end

Note over AnIA: PROCEDIMENTOS/CONTAS
rect rgba(0, 0, 250, .1)
    AnIA->>Caduceus (Consolidação): Procedimentos/Contas
    Note over Caduceus (Consolidação): Detecção de comorbidades e complexidades
    Caduceus (Consolidação)->>HarpIA: Dados consolidados do paciente
    Note over HarpIA: Criação/Atualização de paciente
    HarpIA->>Atlas: Dados consolidados do paciente
    Note over Atlas: Atualização dos dados do paciente
end

Note over AnIA: PROGRAMAS
rect rgba(127, 127, 0, .1)
    AnIA->>HarpIA: Programas
    Note over HarpIA: Criação/Atualização de paciente
    HarpIA->>Atlas: Dados consolidados do paciente
    Note over Atlas: Atualização dos dados do paciente
end

Note over AnIA: CADASTRO
rect rgba(127, 0, 127, .1)
    AnIA->>HarpIA: Dados de Cadastro
    Note over HarpIA: Criação/Atualização de paciente
    HarpIA->>Atlas: Dados consolidados do paciente
    Note over Atlas: Atualização dos dados do paciente
end


:::