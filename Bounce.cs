using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bounce : MonoBehaviour {

        // This is my project WIE
	//Position is based on Gravity and Velocity
	//yPosistion = Vi(t) + 1/2at^2 
	//Think this as 3 dimension variable.  XYZ
	Vector3 ballPosition = new Vector3();
	float gravity = -9.8f;  // remember m/s^2
	float yVelocity; //remember m/s
	float deltaYpos; // This is the difference

	bool bounce = false;

	// Use this for initialization
	void Start () {

		ballPosition = transform.position;
		yVelocity = 10.0f;

		
	}
	
	// Update is called once per frame
	void Update () {


		deltaYpos = (yVelocity * Time.deltaTime) + (0.5f * gravity * Time.deltaTime * Time.deltaTime);

		ballPosition.y = ballPosition.y + deltaYpos;
		yVelocity = yVelocity + (gravity * Time.deltaTime);

		Debug.Log("Position of Sphere:" + ballPosition.y);
		Debug.Log ("Velocity is yVelocity:" + yVelocity);
			
		transform.position = ballPosition;


		if (ballPosition.y <= 0.5f) {
			if (bounce == false) {
				yVelocity = yVelocity * -0.9f;
				bounce = true;
			} else {
				bounce = false;
			}
		}



	}
}
