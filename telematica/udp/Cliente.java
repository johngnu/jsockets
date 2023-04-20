package telematica.udp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Cliente {

	public static void main(String[] args) {
		String mensaje = "Mensaje al servidor";
		String host = "localhost";
		int puerto = 8888;
		try {
			InetAddress dst = InetAddress.getByName(host);
			DatagramSocket miSocket = new DatagramSocket();
			byte[] buffer = mensaje.getBytes();
			DatagramPacket datagrama = new DatagramPacket(buffer, mensaje.length(), dst, puerto);
			miSocket.send(datagrama);
			miSocket.close();
		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}

}
