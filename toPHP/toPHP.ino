#include <WiFiNINA.h>
#include "MPU9250.h"

MPU9250 mpu;


char ssid[] = "Keep Out!!";
char pass[] = "shinypanda172@";

int status = WL_IDLE_STATUS;

char server[] = "http://localhost:3000/welcome.php";

String postData;
String postVariable = "temp=";

WiFiClient client;

void setup() {

  Serial.begin(115200);

  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to Network named: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(10000);
  }

  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());
  IPAddress ip = WiFi.localIP();
  IPAddress gateway = WiFi.gatewayIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  Wire.begin();
  delay(2000);

  MPU9250Setting setting;
  setting.accel_fs_sel = ACCEL_FS_SEL::A16G;
  setting.gyro_fs_sel = GYRO_FS_SEL::G2000DPS;
  setting.mag_output_bits = MAG_OUTPUT_BITS::M16BITS;
  setting.fifo_sample_rate = FIFO_SAMPLE_RATE::SMPL_200HZ;
  setting.gyro_fchoice = 0x03;
  setting.gyro_dlpf_cfg = GYRO_DLPF_CFG::DLPF_41HZ;
  setting.accel_fchoice = 0x01;
  setting.accel_dlpf_cfg = ACCEL_DLPF_CFG::DLPF_45HZ;

  if (!mpu.setup(0x68, setting)) {  // change to your own address
    while (1) {
     Serial.println("MPU connection failed. Please check your connection with `connection_check` example.");
     delay(5000);
     }
  }
}

void loop() {

  if (client.connect(server, 80)) {
    if (mpu.update()){
     client.println("POST /test/post.php HTTP/1.1");
     client.println("Host: www.elithecomputerguy.com");
     client.println("Content-Type: application/x-www-form-urlencoded");
     client.print("Content-Length: ");
     //client.println(postData.length());
     client.println();
     client.print(mpu.getYaw(), 2);
    }
  }

  if (client.connected()) {
    client.stop();
  }
  Serial.println(mpu.getYaw(), 2);

  delay(3000);
}