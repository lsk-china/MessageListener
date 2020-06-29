package com.lsk.messageListener;

import java.io.OutputStream;
import java.net.Socket;

public class ChangeConfig {
    public static void main(String[] args) throws Exception{
        String host = args[0];
        int port = Integer.parseInt(args[1]);
        String properData = args[2];
        Socket socket = new Socket(host,port);
        OutputStream outputStream = socket.getOutputStream();
        outputStream.write(properData.getBytes());
        socket.shutdownOutput();
    }
}
