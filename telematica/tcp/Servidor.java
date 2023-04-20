package telematica.tcp;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Servidor {

	public static void main(String[] args) {
		DataOutputStream out;
		try {
			ServerSocket miSocket = new ServerSocket(9876);
			Socket solic = miSocket.accept();
			out = new DataOutputStream(solic.getOutputStream());
			out.writeUTF("El servidor dice HOLA");
			solic.close();
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}

	}

}
