wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup

echo "733cf126b03f73050e242102592658913d10829a5bf056ab77e7f864b3f8de1f  mariadb_repo_setup" \
    | sha256sum -c -
apt update
chmod +x mariadb_repo_setup
sudo apt install -y curl libmariadb3 libmariadb-dev python3-pip

sudo ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.6"


pip3 install -r requirements
