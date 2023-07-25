install_termux() {
    pkg update
    pkg upgrade
    pkg install git
    git clone https://github.com/DX4GREY/YouTube-To-MP3
    cd YouTube-To-MP3
    sh setup.sh
    cd ../
    rm -rf YouTube-To-MP3
}
install_linux() {
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install git
    git clone https://github.com/DX4GREY/YouTube-To-MP3
    cd YouTube-To-MP3
    sh setup.sh
    cd ../
    sudo rm -rf YouTube-To-MP3
}

detect_platform() {
    platform=$(uname -o)
    case $platform in
        "Android")
            install_termux
            ;;
        "GNU/Linux")
            install_linux
            ;;
        *)
            echo "Unsupported platform: $platform"
            ;;
    esac
}
detect_platform
