echo "Hello. Now I download chat-server and chat-client in your computer"
echo "#Command for Python chat" >> ~/.bashrc
echo "alias chat='python3 $pwd/PythonChat/client.py'" >> ~/.bashrc
echo "alias chat-server='python3 $pwd/PythonChat/server.py'" >> ~/.bashrc
chmod +x ~/.bashrc
./.bashrc

