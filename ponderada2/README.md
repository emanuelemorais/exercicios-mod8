# Ponderada 2 - Módulo 8
## Aluno: Emanuele Lacerda Morais Martins

### Pacode de Mapeamento

O pacote de mapeamento se encontra no diretório `exercicios-mod8/ponderada2/src/mapeamento`. 

Para executa-lo é preciso seguir as seguintes instruções:

- Abra o diretório `exercicios-mod8/ponderada2/` e execute o comando abaixo:

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
ros2 launch mapeamento map_launch.py
```

Após a realização desses passos o Gazebo, RVIZ e Teleop serão abertos para realizar a etapa de mapeamento.

#### Video do mapeamento
Neste [link](https://drive.google.com/file/d/1FmcyqAGYNaPYkEmFC-tHm2W3tF0sR89Q/view) é possível ver o funcionamento do pacote.


### Pacote de Navegação

O pacote de mapeamento se encontra no diretório `exercicios-mod8/ponderada2/src/navegacao`. 

Para executa-lo é preciso seguir as seguintes instruções:

- Abra o diretório `exercicios-mod8/ponderada2/` e execute o comando abaixo:

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
ros2 launch navegacao nav_launch.py
```

Após a realização desses passos o Gazebo, RVIZ e um terminal executando o script criado para navegação serão abertos para realizar a etapa de mapeamento.

#### Disclaimer

> O código feito está utilizando um mapa salvo na raiz do projeto, nomeado de `gazebo.yaml` e `gazebo.pgm`.  Caso queira mudar o path ou o mapa que será utilizado é necessário acessar o arquivo no diretório `exercicios-mod8/ponderada2/src/navegacao/launch/nav_launch.py` e na linha 19 mudar o path/mapa utilizado. 

#### Video do mapeamento
Neste [link](https://drive.google.com/file/d/10xD0X_FvuaA83I4ABn1IIk23XQBS-Bbf/view) é possível ver o funcionamento do pacote. 
Fiz um segundo video com obstaculos adicionais não mapeados, para acessar é só clicar no [link](https://drive.google.com/file/d/1p_xuM8CzBhOtPmnpQaaRKhWAZOfz-qS-/view?usp=sharing)
