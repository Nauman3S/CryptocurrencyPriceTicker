
#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SPI.h>

// Define the number of devices we have in the chain and the hardware interface
// NOTE: These pin numbers will probably not work with your hardware and may
// need to be adapted
#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
#define MAX_DEVICES 4
#define CLK_PIN 18
#define DATA_PIN 23
#define CS_PIN 15

// HARDWARE SPI
MD_Parola P = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);
// SOFTWARE SPI
//MD_Parola P = MD_Parola(HARDWARE_TYPE, DATA_PIN, CLK_PIN, CS_PIN, MAX_DEVICES);

uint8_t scrollSpeed = 100; // default frame delay value
textEffect_t scrollEffect = PA_SCROLL_LEFT;
textPosition_t scrollAlign = PA_LEFT;
uint16_t scrollPause = 2000; // in milliseconds

// Global message buffers shared by Serial and Scrolling functions
#define BUF_SIZE 75
char curMessage[BUF_SIZE] = {""};
char newMessage[BUF_SIZE] = {"Currency PRICE"};
bool newMessageAvailable = true;

void readSerial(void)
{
    static char *cp = newMessage;

    while (Serial.available())
    {
        *cp = (char)Serial.read();
        if ((*cp == '\n') || (cp - newMessage >= BUF_SIZE - 2)) // end of message character or full buffer
        {
            *cp = '\0'; // end the string
            // restart the index for next filling spree and flag we have a message waiting
            cp = newMessage;
            newMessageAvailable = true;
        }
        else // move char pointer to next position
            cp++;
    }
}

void setupLEDMatrix()
{

    Serial.print("\n[Scrolling Display]\nType a message for the scrolling display\nEnd message line with a newline");

    P.begin();
    P.displayText(curMessage, scrollAlign, scrollSpeed, scrollPause, scrollEffect, scrollEffect);
    P.setIntensity(0);
    P.displayClear();
}
void updateMessage(String data)
{
    newMessageAvailable = true;
    //char newMsg[BUF_SIZE] = data.c_str();
    strcpy(curMessage, data.c_str());
}
void loopLEDMatrix()
{

    if (P.displayAnimate())
    {
        if (newMessageAvailable)
        {
            // strcpy(curMessage, newMessage);
            newMessageAvailable = false;
        }
        P.displayReset();
    }
    // readSerial();
}
