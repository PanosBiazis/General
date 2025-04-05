package com.example.myapp;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
//import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
//package com.example.myapplication;

//import android.os.Bundle;
//import android.view.View;
//import android.widget.Button;
//import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Find TextView and Button from the layout
        TextView jtxtMsg = (TextView) findViewById(R.id.textView);
        Button jBtnPress = (Button) findViewById(R.id.button);

        // Set the OnClickListener for the Button
        jBtnPress.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Change the text of the TextView
                jtxtMsg.setText("Welcome to Android Programming!!!");
            }
        });
    }
}