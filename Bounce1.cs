using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bounce : MonoBehaviour {

    Vector3 ballPosition = new Vector3();

    // Use this for initialization
	void Start () {

        ballPosition = transform.position;
	}
	
	// Update is called once per frame
	void Update () {

        ballPosition.y = ballPosition.y - 0.25f;

        transform.position = ballPosition;

		
	}
}