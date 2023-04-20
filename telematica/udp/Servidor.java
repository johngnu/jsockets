package telematica.udp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class Servidor {

	public static void main(String[] args) {
		try {
			DatagramSocket miSocket = new DatagramSocket(8888);
			byte[] buffer = new byte[100];
			DatagramPacket datagrama = new DatagramPacket(buffer, buffer.length);
			miSocket.receive(datagrama);
			String mensaje = new String(buffer);
			System.out.println(mensaje);
			miSocket.close();
		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}

}
