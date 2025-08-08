package com.titanchatx.app

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Simple placeholder UI - replace with actual layout later
        val tv = TextView(this)
        tv.text = "Welcome to TitanChatX (Placeholder)"
        setContentView(tv)
    }
}
