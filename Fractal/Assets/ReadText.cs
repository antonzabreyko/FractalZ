using System.Collections;
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
        LineRenderer lineRenderer = gameObject.AddComponent<LineRenderer>();
        lineRenderer.material = new Material(Shader.Find("Sprites/Default"));
        lineRenderer.widthMultiplier = 0.2f;
        lineRenderer.positionCount = 4;

        float alpha = 1.0f;
        Gradient gradient = new Gradient();
        gradient.SetKeys(
            new GradientColorKey[] { new GradientColorKey(c1, 0.0f), new GradientColorKey(c2, 1.0f) },
            new GradientAlphaKey[] { new GradientAlphaKey(alpha, 0.0f), new GradientAlphaKey(alpha, 1.0f) }
        );
        lineRenderer.colorGradient =gradient;
        var points = new Vector3[4];


        for (int i = 1; i < strings.Count; i++)
        {
            //Debug.Log(strings[i]);
            string[] coordinates = strings[i].Split(',');
            float x = float.Parse(coordinates[0]);
            float y = float.Parse(coordinates[1]);
            points[i] = new Vector3(x, y, 0.0f);
            lineRenderer.SetPositions(points);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
