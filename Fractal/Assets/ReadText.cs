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

        //Read the text from directly from the test.txt file
        StreamReader reader = new StreamReader(path);
        Debug.Log(reader.ReadToEnd());
        reader.Close();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
