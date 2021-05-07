package com.example.imigw;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import androidx.core.app.ActivityCompat;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    public static Context mainActivityContext;

    public static String postUrl = "http://192.168.8.106:5000/user";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        ActivityCompat.requestPermissions(MainActivity.this, new String[]{Manifest.permission.INTERNET}, 0);

        mainActivityContext = this;

        loginActivity();


    }

    private void loginActivity()
    {
        Button btn = (Button) findViewById(R.id.loginBtn);
        btn.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        startActivity(new Intent(MainActivity.this, LoginActivity.class));
                    }
                });
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        TextView responseText = findViewById(R.id.responseText);
        if (requestCode == 2) { // Login
            responseText.setText("Successful Login.");
        } else {
            responseText.setText("Invalid or no data entered. Please try again.");
        }
    }
}