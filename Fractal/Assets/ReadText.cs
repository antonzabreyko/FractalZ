﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System.IO;

public class ReadText : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
        string path = "Assets/Resources/Test.frac";
        List<string> strings = new List<string>();
        //Read the text from directly from the test.txt file
        StreamReader reader = new StreamReader(path);
        while (!reader.EndOfStream)
        {
            strings.Add(reader.ReadLine());
        }
        reader.Close();
        //metadata
        Debug.Log(strings[0]);
        //points

        gameObject.GetComponent<LineRenderer>().material = new Material(Shader.Find("Sprites/Default"));
        gameObject.GetComponent<LineRenderer>().widthMultiplier = 0.2f;
        gameObject.GetComponent<LineRenderer>().positionCount = 5;

        float alpha = 1.0f;
        Gradient gradient = new Gradient();
        gradient.SetKeys(
            new GradientColorKey[] { new GradientColorKey(Color.black, 0.0f), new GradientColorKey(Color.blue, 1.0f) },
            new GradientAlphaKey[] { new GradientAlphaKey(alpha, 0.0f), new GradientAlphaKey(alpha, 1.0f) }
        );
        gameObject.GetComponent<LineRenderer>().colorGradient =gradient;
        var points = new Vector3[strings.Count];
        Debug.Log(strings.Count);

        for (int i = 1; i < strings.Count; i++)
        {
            //Debug.Log(strings[i]);
            
            string[] coordinates = strings[i].Split(',');
            
            float x = float.Parse(coordinates[0]);
            float y = float.Parse(coordinates[1]);

            points[i-1] = new Vector3(x, y, 0.0f);
            //
            
        }

        string[] coordinates1 = strings[1].Split(',');
        float x1 = float.Parse(coordinates1[0]);
        float y1 = float.Parse(coordinates1[1]);
        points[strings.Count - 1] = new Vector3(x1, y1, 0.0f);
        for (int i = 0; i < strings.Count; i++)
        {
            Debug.Log(points[i]);
        }
        gameObject.GetComponent<LineRenderer>().SetPositions(points);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
