#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

// LCD 설정 (I2C 주소: 0x27, 16x2 LCD)
LiquidCrystal_I2C lcd(0x27, 16, 2);

// DHT 센서 설정
#define DHTPIN 2     // DHT 센서 핀
#define DHTTYPE DHT11 // DHT11 또는 DHT22
DHT dht(DHTPIN, DHTTYPE);

// RGB LED 핀 설정
#define RED_LED 3
#define GREEN_LED 4
#define BLUE_LED 5

// 부저 핀 설정
#define BUZZER_PIN 6

// 시간 설정 (시, 분)
int alarm1Hour = 9, alarm1Min = 0;   // 첫 번째 알람 시간
int alarm2Hour = 12, alarm2Min = 30; // 두 번째 알람 시간
int alarm3Hour = 15, alarm3Min = 0;  // 세 번째 알람 시간

void setup() {
  // LCD 초기화
  lcd.init();
  lcd.backlight();
  
  // DHT 센서 초기화
  dht.begin();

  // 핀 모드 설정
  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  // 초기 LCD 메시지
  lcd.setCursor(0, 0);
  lcd.print("Initializing...");
  delay(2000);
  lcd.clear();
}

void loop() {
  // 현재 시간 (예: RTC 모듈 없이 코드로 가정값 사용)
  int currentHour = 9; // 여기에 실제 RTC 값을 넣으세요
  int currentMin = 0;  // 여기에 실제 RTC 값을 넣으세요

  // 온도 및 습도 읽기
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // LCD에 정보 표시
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperature);
  lcd.print(" C");

  lcd.setCursor(0, 1);
  lcd.print("Humidity: ");
  lcd.print(humidity);
  lcd.print(" %");

  // 알람 확인
  if (checkAlarm(currentHour, currentMin, alarm1Hour, alarm1Min)) {
    triggerAlarm(RED_LED); // 빨간색 LED 및 알람
  } else if (checkAlarm(currentHour, currentMin, alarm2Hour, alarm2Min)) {
    triggerAlarm(GREEN_LED); // 초록색 LED 및 알람
  } else if (checkAlarm(currentHour, currentMin, alarm3Hour, alarm3Min)) {
    triggerAlarm(BLUE_LED); // 파란색 LED 및 알람
  } else {
    // LED와 부저 끄기
    digitalWrite(RED_LED, LOW);
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(BLUE_LED, LOW);
    digitalWrite(BUZZER_PIN, LOW);
  }

  delay(1000); // 1초 대기
}

// 알람 확인 함수
bool checkAlarm(int currentHour, int currentMin, int alarmHour, int alarmMin) {
  return (currentHour == alarmHour && currentMin == alarmMin);
}

// 알람 트리거 함수
void triggerAlarm(int ledPin) {
  // LED 켜기
  digitalWrite(ledPin, HIGH);
  
  // 부저 울리기
  for (int i = 0; i < 3; i++) {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(200);
    digitalWrite(BUZZER_PIN, LOW);
    delay(200);
  }
}