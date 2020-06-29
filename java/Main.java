package com.lsk.messageListener;

import javax.swing.*;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Main {
    public static void main(String[] args) throws Exception{
//        InfoUtil tool = new InfoUtil();
//        tool.show("test","test");
        ServerSocket serverSocket = new ServerSocket(11000);
        while(true){
            Socket socket = serverSocket.accept();
            new Thread(new ServerThread(socket)).start();
        }
    }
}
class ServerThread implements Runnable{
    private Socket socket;
    private InfoUtil infoUtil = new InfoUtil();
    public ServerThread(Socket socket){
        this.socket = socket;
    }
    @Override
    public void run() {
        try{
            byte[] buffer = new byte[1024];
            InputStream is = socket.getInputStream();
            int length = 0;
            StringBuilder stringBuilder = new StringBuilder();
            while((length = is.read(buffer)) != -1){
                stringBuilder.append(new String(buffer,0,length));
            }
            System.out.println(stringBuilder.toString());
            //infoUtil.show("Message", stringBuilder.toString());
            String[] datas = stringBuilder.toString().split(",");
            String message = "Comment : "+datas[0]+",\r\nLike : "+datas[1]+",\r\nSystem : "+datas[2];
            infoUtil.show("Message",message);
            socket.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}