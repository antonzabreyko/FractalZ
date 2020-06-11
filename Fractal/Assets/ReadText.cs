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
        for (int i = 1; i < strings.Count; i++)
        {
            //Debug.Log(strings[i]);
            string[] coordinates = strings[i].Split(',');
            int x = Int32.parse(coordinates[0]);
            int y = Int32.parse(coordinates[1]);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
