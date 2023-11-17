# Ponderada 3 - Módulo 8
## Aluno: Emanuele Lacerda Morais Martins

### Como executar o código

O pacote do chatbot se encontra no diretório `exercicios-mod8/ponderada3/src/chatbot`. 

Para executa-lo é preciso seguir as seguintes instruções:

- Abra o diretório `exercicios-mod8/ponderada3/` e execute o comando abaixo:

```
colcon build
```

- Em seguida, no mesmo diretório rode o comando:
```
source install/local_setup.bash
```

Os comando acima irão criar um workspace para que o pacote funcione devidamente.

- Após isso é preciso rodar o comando abaixo:
```
ros2 launch chatbot chatbot_launch.py
```

Após a realização desses passos o Gazebo, RVIZ e um terminal com o chatbot serão abertos para realizar a etapa de mapeamento.

### Video do chatbot funcionando
Neste [link](https://drive.google.com/file/d/1puF9x37-hi9YWKAjKivmNELyLkqulpNB/view?usp=sharing) é possível acessar um video dele funcionando.

### Funcionamento do Chatbot

Para essa atividade 3 pontos foram mapeados, sendo eles `biblioteca`, `secretaria` e `laboratorio`. A imagem abaixo mostra os pontos criados no mapa do gazebo para exemplificar os locais de destino:

![docss](https://github.com/emanuelemorais/exercicios-mod8/assets/99221221/7c5386ce-353c-468c-8bed-13e36246217a)


Para fazer com que o robô vá para algum lugar existe um regex que entende o local indicado. Diversas formas de escrever vão ser entendidas como "Se mova para a biblioteca", "dirija-se a secretaria" entre outros. Quando um ponto de destino não mapeado é solicitado o chatbot ira informar que o local não pode ser encontrado. Além disso, enquanto o robô se move o feedback "Indo..." é exposto até que ele chegue ao destino.
