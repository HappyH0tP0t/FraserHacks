
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ExplodeChildren : MonoBehaviour
{
    void Start()
    {
        foreach (Transform child in transform)
        {
            child.gameObject.GetComponent<Rigidbody>().AddForce((child.position - transform.position).normalized * 250);
            child.gameObject.GetComponent<Rigidbody>().AddTorque(new Vector3(Random.Range(-1f, 1f), Random.Range(-1f, 1f), Random.Range(-1f, 1f))* 200f);
        }
    }
}
