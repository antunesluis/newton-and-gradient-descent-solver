# Estruturas Principais

## QApplication e QPushButton

- QApplication -> O Widget principal da aplicação (contem o loop de eventos da aplicação).
- QPushButton -> Um botão.
- QtWidget -> Genérico.
- QLayout -> Um widget de layout que recebe outros widgets.

## Hierarquia principal e principais elementos

- **QMainWindow** Irá receber o central widget. É usado para fornecer elementos básicos da janela, como status bar e menu.
- **O central_widget**, do tipo QLayout, é um widget genérico e irá receber todos os outros widgets. Deve ter um layout atribuido a ele.
- O central_widget não recebe widgets, e por isso o layout deve ser criado para realizar essa função de receber os widgets.
- O **layout**, que recebe qualquer um dos tipos de layout, é o principal widget e irá determinar a organização dos widgets.

```python
window = QMainWindow()
central_widget = QWidget()
layout = QvBoxLayout()

window.setCentralWidget(central_widget)
central_widget.setLayout(layout)

layout.addWidget(botao_generico);
window.show()
```

```
-> QApplication
    -> QMainWindow
        ->central_widget
            -> layout
             -> Widget
             -> Widget
             -> Widget
    -> show
-> exec
```

## Signals e Slots

- **slots** é um método que é executado quando um trigger é disparado.
- O looping da aplicação fica interruptamente procurando por eventos (clicar em botões, opções marcadas, etc). Quando eu quero me conectar a um evento especifico eu indico o **signal** de disparo (clicado, selecionado, tecla digitada, etc) e indico a qual **slot** essa ação está conectada, ou seja, **o que ocorre quando a ação é realizada.**
- Quando eu me conecto a ações eu tenho uma resposta de quando elas ocorrem, e então eu me conecto a funções especificas, que recebem o nome de **signals**.
