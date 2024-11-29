using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class Game : MonoBehaviour
{
    [Header("Game vraibles")]
    public string difficulty = "easy";
    public LayerMask targetMask;
    public GameObject targetPrefab;
    public GameObject shatteredPrefab;
    public GameObject firework;
    public int amountOfTargets = 0;

    public float currentNumber = 0f;
    public int goalNumber = 0;
    public float stopwatch = 0f;

    public float lowestTime = 100000f;
    public float turningSensitivity = 0.2f;

    [Header("UI")]
    public TextMeshProUGUI topText;
    public TextMeshProUGUI numbersText;

    [Header("Shake")]
    public float shakeTimeLeft = 0f;
    public float timeSinceShook = 0f;
    public Vector3 originalPosition;

    void Start()
    {
        originalPosition = Camera.main.transform.position;
        currentNumber = Random.Range(0, 100);
        goalNumber = Random.Range(0, 100);
        stopwatch = 0f;
        for (int i = 0; i < 5; i++)
        {
            GameObject targetInstance = Instantiate(targetPrefab, new Vector3(Random.Range(-2f, 2f), Random.Range(-2f, 2f), Random.Range(-1f, 1f)), Quaternion.identity);
            amountOfTargets++;
        }
    }

    void Update()
    {
        shakeTimeLeft -= Time.deltaTime;
        timeSinceShook += Time.deltaTime;
        stopwatch += Time.deltaTime;
        if (Input.GetMouseButtonDown(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            if (Physics.Raycast(ray, out RaycastHit hit, Mathf.Infinity, targetMask))
            {
                amountOfTargets--;
                GameObject targetInstance = hit.collider.gameObject.transform.parent.gameObject;
                string operatorType = targetInstance.GetComponent<Target>().operatorType;
                int operatorNumber = targetInstance.GetComponent<Target>().operatorNumber;
                if (operatorType == "+")
                {
                    currentNumber += operatorNumber;
                }
                if (operatorType == "-")
                {
                    currentNumber -= operatorNumber;
                }
                if (operatorType == "*")
                {
                    currentNumber *= operatorNumber;
                }
                if (operatorType == "/")
                {
                    currentNumber /= operatorNumber;
                }
                currentNumber = Mathf.Max(Mathf.Floor(currentNumber), 0f);
                Instantiate(shatteredPrefab, targetInstance.transform.position, targetInstance.transform.rotation);
                Destroy(targetInstance);
                Instantiate(targetPrefab, new Vector3(Random.Range(-2f, 2f), Random.Range(-2f, 2f), Random.Range(-1f, 1f)), Quaternion.identity);
                shakeTimeLeft = 0.1f;
                timeSinceShook = 0f;
            }
        }
        if (currentNumber == goalNumber || Input.GetKeyDown(KeyCode.RightControl))
        {
            Debug.Log("you won");
            currentNumber = Random.Range(0, 100);
            goalNumber = Random.Range(0, 100);
            if (stopwatch < lowestTime)
            {
                lowestTime = stopwatch;
            }
            GameObject fireworkInstance = Instantiate(firework);
            Destroy(fireworkInstance, 5);
            stopwatch = 0f;
        }
        if (shakeTimeLeft >= 0)
        {
            Camera.main.transform.position = originalPosition + new Vector3(Random.Range(-1f, 1f), Random.Range(-1f, 1f), Random.Range(-1f, 1f)) * 0.2f * (Mathf.Clamp(timeSinceShook, 0, 0.15f) / 0.15f);
        }
        else
        {
            Camera.main.transform.position = originalPosition;
        }
        topText.text = "Time: " + (Mathf.Round(stopwatch * 1000f) / 1000f).ToString() + "\nBest Time: " + (Mathf.Round(lowestTime * 1000f) / 1000f).ToString();
        numbersText.text = "Current: " + currentNumber.ToString() + " Goal: " + goalNumber.ToString();
        Camera.main.transform.rotation = Quaternion.Euler(new Vector3((-Input.mousePosition.y + Screen.height / 2) * turningSensitivity, (Input.mousePosition.x - Screen.width / 2) * turningSensitivity, 0));
    }
}
