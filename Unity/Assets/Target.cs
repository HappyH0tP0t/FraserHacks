using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class Target : MonoBehaviour
{
    public string operatorType = "";
    public int operatorNumber = 0;
    public TextMeshPro text;

    void Start()
    {
        GameObject game = GameObject.Find("Game");
        operatorNumber = Random.Range(1, 10);
        string[] possibleOperators = new string[] {"+", "-", "*", "/"};
        int sign = (int)Mathf.Sign(game.GetComponent<Game>().goalNumber - game.GetComponent<Game>().currentNumber);
        if (sign < 0)
        {
            if (game.GetComponent<Game>().difficulty == "easy")
            {
                possibleOperators = new string[] {"+", "-", "*", "/", "-", "-", "-", "/", "/", "/", };
            }
            else
            {
                possibleOperators = new string[] {"+", "-", "*", "/", "+", "+", "+", "*", "*", "*", "^", "√"};
            }
        }
        else
        {
            if (game.GetComponent<Game>().difficulty == "easy")
            {
                possibleOperators = new string[] {"+", "-", "*", "/", "+", "+", "+", "*", "*", "*", };
            }
            else
            {
                possibleOperators = new string[] {"+", "-", "*", "/", "-", "-", "-", "/", "/", "/", "^", "√"};
            }
        }
        operatorType = possibleOperators[Random.Range(0, possibleOperators.Length)];
    }

    void Update()
    {
        text.text = operatorType + operatorNumber.ToString();
    }
}
