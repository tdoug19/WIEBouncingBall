using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bounce : MonoBehaviour {

    Vector3 ballPosition = new Vector3();
    float gravity = -9.8f;  //m/s^2
    float yVelocity;  //m/s
    float deltaYpos;  //Difference between frames

    // Use this for initialization
	void Start () {

        ballPosition = transform.position;

	}
	
	// Update is called once per frame
	void Update () {

        //x = Vi(t) = 1/2 at^2

        deltaYpos = (yVelocity * Time.deltaTime)
            + (0.5f * gravity * Time.deltaTime * Time.deltaTime);


        ballPosition.y = ballPosition.y + deltaYpos;
        yVelocity = yVelocity + (gravity * Time.deltaTime);

        Debug.Log("Velocity is yVelocity" + yVelocity);
        transform.position = ballPosition;

		
	}
}
