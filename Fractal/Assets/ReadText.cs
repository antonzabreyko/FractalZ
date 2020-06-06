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
        
        string path = "Assets/Resources/test";
        List<string> strings = new List<string>();
        //Read the text from directly from the test.txt file
        StreamReader reader = new StreamReader(path);
        while (!reader.EndOfStream)
        {
            strings.Add(reader.ReadLine());
            
        }
        reader.Close();
        for (int i = 0; i < strings.Count; i++)
        {
            Debug.Log(strings[i]);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
