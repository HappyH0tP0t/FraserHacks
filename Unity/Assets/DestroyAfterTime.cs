using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyAfterTime : MonoBehaviour
{
    public Vector2 timeRange;
    public float timeToDestroy;
    public float timeSinceStart = 0f;

    public float timeItTakesToGetObliterated = 2f;

    void Start()
    {
        timeToDestroy = Random.Range(timeRange.x, timeRange.y);
    }

    void Update()
    {
        timeSinceStart += Time.deltaTime;
        if (timeSinceStart > timeToDestroy)
        {
            transform.localScale -= Vector3.one * (1 / timeItTakesToGetObliterated) * Time.deltaTime;
            if (transform.localScale.x <= 0.1f)
            {
                Destroy(gameObject);
            }
        }
    }
}
