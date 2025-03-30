const express = require("express");
const puppeteer = require("puppeteer");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/search", async (req, res) => {
  const query = req.query.q;
  if (!query) {
    return res.status(400).json({ error: "Missing search query" });
  }

  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(`https://www.google.com/search?q=${query}`);

  const results = await page.evaluate(() =>
    Array.from(document.querySelectorAll("h3")).map((el) => el.innerText)
  );

  await browser.close();
  res.json({ results });
});

const PORT = process.env.PORT || 5001; // Change 5000 to 5001

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

