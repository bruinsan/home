## Install ZSH

```bash
sudo apt-get install zsh
```

## Install Oh My ZSH

```bash
cd
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## Setup missing fonts (powerline)

### Install powerline font
```bash
cd
wget https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf
wget https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf
mv PowerlineSymbols.otf ~/.fonts/
mkdir -p .config/fontconfig/conf.d 
```

### Clean fonts cache
```bash
fc-cache -vf ~/.fonts/
```

### Move config file
```bash
mv 10-powerline-symbols.conf ~/.config/fontconfig/conf.d/
```

## Configure ZSH

### Theme
Change [ZSH_THEME="robbyrussell"] to [ZSH_THEME="agnoster"]
```bash
sed -i 's/robbyrussell/agnoster/g' ~/.zshrc
```

#### Change directory colors to solarize
```bash
mkdir ~/.solarized
wget https://raw.githubusercontent.com/seebi/dircolors-solarized/master/dircolors.ansi-dark
mv dircolors.ansi-dark .solarized
echo "eval \`dircolors ~/.solarized/dircolors.ansi-dark\`" >> ~/.zshrc
```
### Set ZSH as default shell
```bash
chsh -s $(which zsh)
```

> Restart Terminal and you're done!

### That's it!
