# 📦 Sistema de Entregas em Python

Este projeto é um sistema simples de console que simula diferentes formas de entrega, permitindo ao usuário escolher o tipo de serviço e consultar **prazo** ou **preço** de cada modalidade.

Ele foi desenvolvido com foco em **Programação Orientada a Objetos (POO)** e no uso de **classes abstratas** para simular o uso de **interfaces**

---

## 🚀 Funcionalidades

- Permite escolher entre três tipos de entrega:
  - **Motoboy**
  - **Drone**
  - **Correios**
- Para cada tipo de entrega, o usuário pode:
  - 📅 Consultar o **prazo de entrega**
  - 💰 Consultar o **valor do frete**
- Interface em modo texto (terminal).
- Sistema de menu com repetição usando `while`, permitindo novas consultas sem reiniciar o programa.
- Opção para sair do sistema a qualquer momento.
- Validação de entradas para evitar erros.

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foi possível praticar e compreender:

- **Classes Abstratas (`ABC`)**  
  Garantem que toda classe de entrega implemente os métodos `calcular_prazo()` e `calcular_preco()`.

- **Polimorfismo**  
  O mesmo método (`calcular_prazo` e `calcular_preco`) se comporta de forma diferente dependendo do tipo de entrega escolhido.

- **Herança**  
  As classes `EntregaMotoboy`, `EntregaDrone` e `EntregaCorreios` herdam da classe base `Entrega`.

- **Dicionários como “menu de opções”**  
  Uso de um dicionário para mapear as letras (`m`, `d`, `c`) aos objetos de cada tipo de entrega.

- **Estrutura de repetição (`while`)**  
  Mantém o sistema ativo até que o usuário escolha sair.

- **Condicionais (`if/elif/else`)**  
  Controlam o fluxo do programa com base na escolha do usuário.

- **Boas práticas de organização**  
  Separação clara entre regras de negócio (classes) e interação com o usuário (menu).
