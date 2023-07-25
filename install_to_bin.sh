detect_platform() {
    platform=$(uname -o)
    case $platform in
        "Android")
            install_termux
            ;;
        "GNU/Linux")
            install_linux
            ;;
        "Ubuntu")
            install_linux
            ;;
        *)
            echo "Unsupported platform: $platform"
            ;;
    esac
}
install_linux(){
    sudo echo "sudo python $HOME/.ytmp3/main.py \$1 \$2 \$3 \$4 \$5" > $HOME/.local/bin/ytmp3
    sudo echo 'echo "Uninstalling ytmp3..." && sudo rm -rf $HOME/.ytmp3 && sudo rm -rf $HOME/.local/bin/ytmp3 && sudo rm -rf $HOME/.local/bin/ytmp3-uninstaller && echo "ytmp3 uninstall task done"' > $HOME/.local/bin/ytmp3-uninstaller
    sudo cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.ytmp3"
    sudo chmod +x $HOME/.local/bin/ytmp3
    sudo chmod +x $HOME/.local/bin/ytmp3-uninstaller
}
install_termux(){
    cp -r "$(cd "$(dirname "$0")" && pwd)/module" "$HOME/.ytmp3"
    echo "python $HOME/.ytmp3/main.py \$1 \$2 \$3 \$4 \$5" > $PREFIX/bin/ytmp3
    echo 'echo "Uninstalling ytmp3..." && rm -rf $HOME/.ytmp3 && rm -rf $PREFIX/bin/ytmp3 && rm -rf $PREFIX/bin/ytmp3-unisntaller && echo "ytmp3 uninstall task done"' > $PREFIX/bin/ytmp3-uninstaller
    chmod +x $PREFIX/bin/ytmp3
    chmod +x $PREFIX/bin/ytmp3-uninstaller
}
detect_platform